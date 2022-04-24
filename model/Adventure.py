'''
    @filename : Adventure.py
    @author : JunHyeon.Kim
    @email : sleep4725@naver.com
    @date : 20220423
    @package: naver.model
'''
import os  
import sys
PROJ_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJ_ROOT_PATH)

from urllib.parse import urlencode
from common.Common import Common

##
# Adventure 
# https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cnt&date=20220422&tg=6
## 
class ModelAdventure(Common):
    
    FLAG = "adventure"
     
    def __init__(self) -> None:
        Common.__init__(self, flag=ModelAdventure.FLAG)
        self.urlParams = urlencode({
            "sel": "cnt",
            "tg": 6
        })