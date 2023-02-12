def get_user_details(user):            
    user_response = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone': user.phone,
        'email': user.email,
        'address': user.address,
        #'profile_photo': None if user.profile_photo is None else user.profile_photo.url,
        'date_joined': user.date_joined,
        'date_of_birth': user.date_of_birth
    }
    return user_response