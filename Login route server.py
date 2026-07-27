# =====================================
# REGISTER DEVICE FOR PUSH NOTIFICATION
# =====================================


@app.post("/device/register")
def register_user_device(

    data:dict = Body(...)

):


    username = data.get(
        "username"
    )


    token = data.get(
        "token"
    )


    if not username or not token:

        raise HTTPException(

            status_code=400,

            detail="Missing username or token"

        )


    return register_device(

        username,

        token

    )
