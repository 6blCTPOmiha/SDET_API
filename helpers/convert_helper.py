import json
from models.entity_model import EntityModelResponse



class ConvertHelper:

    @staticmethod
    def deserialize_response(response_text: str) -> EntityModelResponse:
        """Десериализация API в Pydantic"""
        try:
            json_data = json.loads(response_text)
            entity = EntityModelResponse(**json_data)
            return entity
        except Exception as e:
            print(f"\nОшибка: {e}")
            raise

    @staticmethod
    def deserialize_responses(response_text: str) -> list[EntityModelResponse]:
        """API в список Pydantic моделей"""
        try:
            json_data = json.loads(response_text)
            entities_data = json_data["entity"]
            entities = [EntityModelResponse(**entity_data) for entity_data in entities_data]
            return entities
        except Exception as e:
            print(f"\nОшибка: {e}")
            raise
