from beet import Context
from simple_item_plugin.types import NAMESPACE, Lang
from simple_item_plugin.item import Item


def beet_default(ctx: Context):
    print("Hello, world!")
    graplin = Item(
        id="graplin",
        item_name=(
            f"{NAMESPACE}.item.graplin",
            {Lang.en_us: "Graplin", Lang.fr_fr: "Graplin"},
        ),
    ).export(ctx)
