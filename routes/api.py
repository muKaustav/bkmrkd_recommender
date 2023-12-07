from ml import *
from fastapi import APIRouter, HTTPException, Body
from starlette.responses import JSONResponse
from schemas.request import Request
from worker.tasks import ml_task


api = APIRouter()


@api.get("/")
async def home():
    response = {
        "message": "Success",
        "data": "Welcome to BKMRKD Recommendation API",
    }

    return JSONResponse(
        status_code=200, media_type="application/json", content=response
    )


@api.post("/")
async def recommend(request: Request = Body(...)):
    try:
        book_id = int(request.book_id)

        print(book_id)

        ml_task.delay(book_id)

        response = {
            "message": "Success",
            "data": {"book_id": book_id},
        }

        return JSONResponse(
            status_code=200, media_type="application/json", content=response
        )

    except Exception as e:
        print(e)

        response = {
            "message": "Internal Server Error",
            "data": {},
        }

        return JSONResponse(
            status_code=500, media_type="application/json", content=response
        )


# @app.route("/", methods=["GET"])
# def home():
#     request_data = request.get_json()

#     if "url" in request_data:
#         try:
# book_id = int(request_data["url"])
# desc = df_books_processed.loc[
#     df_books_processed["book_id"] == book_id, "book_description"
# ].values[0]

# print(desc)

# rec_data = search(desc)

# data = []

# for _, row in rec_data.iterrows():
#     temp = {
#         "book_id": row["book_id"],
#         "book_name": row["title_without_series"],
#     }

#     data.append(temp)

# return data


#     except ValueError:
#         return jsonify({"error": 'Invalid value for "url". Must be an integer.'})
# else:
#     return jsonify({"error": 'Missing "url" in the request body'})
