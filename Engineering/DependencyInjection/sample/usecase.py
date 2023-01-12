# ① injectorモジュールからinjectデコレータをインポート
from injector import inject

from animal import Animal
from vehicle import Vehicle

class UseCase():
    
    # 依存先オブジェクトの注入対象であることをinjectデコレータで宣言
    @inject
    def __init__(self, animal: Animal, vehicle: Vehicle) -> None: # ③型アノテーションは必須
        self.animal = animal 
        self.vehicle = vehicle
    
    def action(self) -> None:
        print(f'{self.animal.cry()}')
        self.vehicle.accelerate()
        self.vehicle.accelerate()
        self.vehicle.accelerate()
        self.vehicle.accelerate()
        print(f'{self.vehicle.speed}')