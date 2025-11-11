from models.addition_model import AdditionModelRequest
from models.entity_model import EntityModelRequest

titles = ['Заголовок сущности', 'Заголовок предмета', 'Заголовок вещи', 'Подголовок сущности', 'Подголовок предмета', 'Подголовок вещи', 'Головок сущности', 'Головок предмета', 'Головок вещи']
verifieds = [True, False]
additional_infos = ['Дополнительные сведения', 'Обвинительные сведения', 'Невероятные сведения', 'Дополнительные улики', 'Обвинительные улики', 'Невероятные улики', 'Дополнительные находки', 'Обвинительные находки', 'Невероятные находки']
additional_numbers = [111, 222, 333, 444, 555, 666, 777, 888, 999]
important_numbers = [[123, 132, 134], [223, 232, 234], [323, 332, 334], [423, 432, 434], [523, 532, 534], [623, 632, 634], [723, 732, 734], [823, 832, 834], [923, 932, 934]]

AMREQ0 = AdditionModelRequest(
    additional_info=additional_infos[0],
    additional_number=additional_numbers[0],
)

EMREQ0 = EntityModelRequest(
    title=titles[0],
    verified=verifieds[0],
    addition=AMREQ0,
    important_numbers=important_numbers[0]
)
