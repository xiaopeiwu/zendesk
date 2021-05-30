from src.conductor import Conductor
import click

FILE_PATHS = {
    "tickets": "data/tickets.json",
    "users": "data/users.json",
    "organizations": "data/organizations.json"
}


@click.group()
def cli():
    """This is a command line tool to search for Zendesk data."""
    pass


@click.command()
@click.option("-d", "--data", type=click.Choice(["users", "organizations", "tickets"], case_sensitive=False),
              default="users", help="dataset to search on")
@click.option("-f", "--field", default="_id", help="field to search for")
@click.option("-v", "--value", default="", help="value to search for")
def search(data, field, value):
    """search on a specified dataset with a value for a certain field"""
    zendesk_search = Conductor(FILE_PATHS, data, field, value)

    click.echo("Loading data...\n")
    zendesk_search.load_all_data()

    for d_type, path in FILE_PATHS.items():
        click.echo(f"{d_type.capitalize()} data loaded from {path}")
    click.echo("\n", nl=False)

    display_value = value if value else "empty"
    click.echo(f"Searching {data} for {field} with the value {display_value}...\n")
    result = zendesk_search.match()
    if result is None:
        click.echo(f"'{field}' is not a valid field for {data}.")
        zendesk_search.list_searchable_fields(data)
    else:
        if result:
            click.echo(f"Found {len(result)} result(s):\n")
            zendesk_search.print_results()
        else:
            click.echo(f"Sorry, no results found for this search.")


@click.command()
@click.option("-d", "--data", type=click.Choice(["users", "organizations", "tickets", "all"], case_sensitive=False),
              default="all", help="dataset whose fields will be listed")
def fields(data):
    """lists all searchable fields for a certain dataset"""
    zendesk_data = Conductor(FILE_PATHS)
    zendesk_data.list_searchable_fields(data)


cli.add_command(search)
cli.add_command(fields)

if __name__ == '__main__':
    cli()
