from __future__ import annotations

from tqdm import tqdm

import scryfall
from mtgproxies.decklists.decklist import Decklist


def fetch_scans_scryfall(decklist: Decklist, separate: bool) -> list[list[str]]:
    """Search Scryfall for scans of a decklist.

    Args:
        decklist: List of (count, name, set_id, collectors_number)-tuples

    Returns:
        List: List of image files
    """
    if separate:
        list_result = []
        for card in tqdm(decklist.cards, desc="Fetching artwork"):
            for index, image_uri in enumerate(card.image_uris):
                if index >= len(list_result):
                    list_result.append([])
                list_result[index].extend([scryfall.get_image(image_uri["png"], silent=True)] * card.count)
        return list_result
    else:
        return [[
            scan
            for card in tqdm(decklist.cards, desc="Fetching artwork")
            for image_uri in card.image_uris
            for scan in [scryfall.get_image(image_uri["png"], silent=True)] * card.count
        ]]
