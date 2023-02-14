from PIL import Image
from rdkit import Chem
from rdkit.Chem import Draw

from rdkit.Chem.SaltRemover import SaltRemover
from rdkit import Chem
from rdkit.Chem import Descriptors

import numpy as np
import torchvision.transforms as transforms

IMG_SIZE = 224
ORGANIC_ATOM_SET = set([5, 6, 7, 8, 9, 15, 16, 17, 35, 53])
REMOVER = SaltRemover()


class ImageData:
    def __init__(self):
        """
        Loads an image and transforms it
        """
        self.normalize = transforms.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
        )
        self._image_transformer = transforms.Compose(
            [transforms.CenterCrop(IMG_SIZE), transforms.ToTensor()]
        )

    def get_image(self, filename):
        img = Image.open(filename).convert("RGB")
        data = self._image_transformer(img)
        data = self.normalize(data)
        data.resize_(1, 3, IMG_SIZE, IMG_SIZE)
        return data


def smiles_to_image(smi, size=IMG_SIZE, savePath=None):
    """
    smis: e.g. COC1=C(C=CC(=C1)NS(=O)(=O)C)C2=CN=CN3C2=CC=C3
    path: E:/a/b/c.png
    """
    try:
        mol = Chem.MolFromSmiles(smi)
        img = Draw.MolsToGridImage([mol], molsPerRow=1, subImgSize=(size, size))
        if savePath is not None:
            img.save(savePath)
        return img
    except Exception as err:
        print(err)
        return None
