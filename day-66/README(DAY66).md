# Cafe API - Day 66

Flask + SQLAlchemy REST API for managing a cafe database.

## Endpoints

### Add a Cafe
`POST /add`

Creates a new cafe record.

- **Content type:** `multipart/form-data`
- **Fields:** `name`, `map_url`, `img_url`, `loc`, `seats`, `has_toilet`, `has_wifi`, `has_sockets`, `can_take_calls`, `coffee_price`
- **Boolean encoding:** use `1` for true and `0` for false on `has_toilet`, `has_wifi`, `has_sockets`, and `can_take_calls`

### Update Cafe Price
`PATCH /update-price/<int:cafe_id>?new_price=<value>`

Updates the coffee price of the cafe identified by the path ID.

- **Required query parameter:** `new_price`
- **Example:** `PATCH /update-price/90?new_price=$4`
- Returns 404 if no cafe matches the given ID.

### Delete a Closed Cafe
`DELETE /report-closed/<int:cafe_id>`

Reports and deletes a closed cafe identified by its path ID.

- **Required body field:** `api-key`, sent as URL-encoded form data
- **Example:** `DELETE /report-closed/88`
- Errors occur when the ID is not found or the API key is missing/invalid.
