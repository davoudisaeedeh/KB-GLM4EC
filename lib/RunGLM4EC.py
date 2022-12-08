import platform
print("python version " + platform.python_version())
import sys
import logging
from configparser import ConfigParser
config = ConfigParser()
config.read("../local_config.cfg")
paths = config.get("script", "syspaths").split(";")
for path in paths:
    sys.path.append(path)
from GLM4EC.glm4ecmodule import GLM4ECModule

glm4ec = GLM4ECModule("GLM4ECModule","../data/","../",{})

glm4ec.annotate_proteins({"proteins":{"A0A7J3ALL0":"MVIVLSRTIRAIAVDVDGTLTDTSRKVSCPAIEALRRQADKGIIVMLVTGNVLPIAYALRHYLGMNGPVIAENGGIVYHDEHVHYLSSKDEPQKAFDQLSKSMKVERIFSDRWRETEIAIRPTYDIELIRKHVRGFDVKVLPSGWAHHLMHKDTDKAKALKWICDNWLRIDMEHVAAIGDSDNDYRMIEIAGFGATPANGSQKCKERADYVASRPYGDGIVEILRVLGLEP", "A0A820Q4W8":"MNININSSLKKLICNARMGKLRQKEREVAARASAAEIYYVSQRTLRYTIRNPVLFLAQVVVAIVLGLVVGFVFNSLEKSIDPGIQNRLGAIFFMVVSQTLGTITSLEPLIKKRVSYIHKTISAYYRTTTFFIVKVICDVLSMRIVSSILFSLIAYCMTGLEQSAG", "A0A7Z7NP06":"MASQSPAPQRADLLFRHATVVDGTGATRRTADVAVTGDRIIAVGDCAGIAADHTVDCSGRVLAPGFIDAHTHDDGYLLVHRDMTPKVSQGITTVVTGNCGISVAPLVSGAPPQPLDLLGPPALFRFDTFAQWLDALRAAPANVNVVPLLGHSTLRVRAMPELDRPANDAEIAAMRDEVRLAMEAGAFGVSTGTFYPPAAAATEAEIVAVCGPVRSHGGIYSTHLRDETDAIVPSIEEALRIGRALDCPVVFSHHKVAGKRNHGRSVETLGLLAEAARLQPLCLDCHPYPATSTMLRLDRVRQSTRTLITWSTGYPAAGGRDFHELMQELGLDEEALLARLRPAAAIYFIMDERDVARIAQFPLTIFGSDGLPFDPRPHPRQWGTFPRILARMVREDQLMTLEAAIHKMSGLAAQQYGLEDRGRIAPGAFADLVLFDAGRVQDRATFEDPLQLSTGIDGVWVNGAQVWQQSARDGAGDTAGSALPAFSGRVLRRLASDNPSAARR"}})

