from fastapi import HTTPException
from app.models.category import Category
from app.repositories.category_repo import CategoryRepository


class CategoryService:

    @staticmethod
    def create(db, payload):
        category = Category(
            name=payload.name,
            description=payload.description
        )
        return CategoryRepository.create(db, category)

    @staticmethod
    def get_all(db):
        return CategoryRepository.get_all(db)

    @staticmethod
    def get_by_id(db, category_id):
        category = CategoryRepository.get_by_id(db, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category

    @staticmethod
    def delete(db, category_id):
        category = CategoryRepository.get_by_id(db, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        CategoryRepository.delete(db, category)
        return {"message": "Category deleted successfully"}