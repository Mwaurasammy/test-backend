# swagger_spec.py

sign_up_spec = {
    'tags': ['Auth'],
    'description': 'Register a new user.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'password': {'type': 'string'}
                },
                'required': ['name', 'email', 'password']  # Specify required fields
            }
        }
    ],
    'responses': {
        '201': {'description': 'User created successfully.'},
        '400': {'description': 'All fields are required.'},
        '409': {'description': 'User already exists.'}
    },
    'produces': ['application/json'],  # Response format
    'consumes': ['application/json'],   # Request format
}

login_spec = {
    'tags': ['Auth'],
    'description': 'Log in a user.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'password': {'type': 'string'}
                },
                'required': ['name', 'password']  # Specify required fields
            }
        }
    ],
    'responses': {
        '200': {'description': 'User logged in successfully.'},
        '400': {'description': 'Missing name or password.'},
        '401': {'description': 'Unauthorized.'}
    },
    'produces': ['application/json'],  # Response format
    'consumes': ['application/json'],   # Request format
}

logout_spec = {
    'tags': ['Auth'],
    'description': 'Log out the current user.',
    'responses': {
        '200': {'description': 'Logged out successfully.'}
    }
}

checksession_spec = {
    'tags': ['Auth'],
    'description': 'Check if there is an active session.',
    'responses': {
        '200': {'description': 'User session is active.'},
        '401': {'description': 'No active session.'}
    }
}

user_profile_spec = {
    'tags': ['User Profile'],
    'description': 'Manage user profiles.',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'The ID of the user'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'The name of the user',
                    },
                    'email': {
                        'type': 'string',
                        'description': 'The email of the user',
                    },
                    'password': {
                        'type': 'string',
                        'description': 'The new password for the user',
                    }
                },
                'required': ['name', 'email']  # Specify required fields
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'User data retrieved/updated successfully.',
            'schema': {
                'type': 'object',
                'properties': {
                    'user': {
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string'},
                            'email': {'type': 'string'},
                        }
                    }
                }
            }
        },
        '404': {
            'description': 'User not found.'
        }
    },
    'produces': ['application/json'],  # Response format
    'consumes': ['application/json'],   # Request format
}

subscription_list_spec = {
    'tags': ['Subscriptions'],
    'description': 'Create or list user subscriptions.',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'The ID of the user'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'description': 'Name of the subscription'},
                    'category': {'type': 'string', 'description': 'Category of the subscription'},
                    'cost': {'type': 'number', 'format': 'float', 'description': 'Cost of the subscription'},
                    'billing_cycle': {'type': 'string', 'description': 'Billing cycle of the subscription (e.g., Monthly)'},
                    'date_of_payment': {'type': 'string', 'format': 'date', 'description': 'Date of payment for the subscription'}
                },
                'required': ['name', 'category', 'cost', 'billing_cycle', 'date_of_payment']
            }
        }
    ],
    'responses': {
        '200': {'description': 'List of subscriptions retrieved successfully.'},
        '201': {'description': 'Subscription created successfully.'},
        '404': {'description': 'User not found.'},
        '415': {'description': 'Unsupported media type. Ensure Content-Type is application/json.'}
    },
    'consumes': ['application/json'],
    'produces': ['application/json']
}



subscription_index_spec = {
    'tags': ['Subscriptions'],
    'description': 'Delete a specific subscription.',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'The ID of the user'
        },
        {
            'name': 'subscription_id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'The ID of the subscription'
        }
    ],
    'responses': {
        '200': {'description': 'Subscription deleted successfully.'},
        '404': {'description': 'Subscription not found.'}
    }
}
