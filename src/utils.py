def get_random_response(input_statement, response_list, storage=None):
    """
    :param input_statement: A statement, that closely matches an input to the chat bot.
    :type input_statement: Statement
    :param response_list: A list of statement options to choose a response from.
    :type response_list: list
    :param storage: An instance of a storage adapter to allow the response selection
                    method to access other statements if needed.
    :type storage: StorageAdapter
    :return: Choose a random response from the selection.
    :rtype: Statement
    """
    from random import choice

    return choice(response_list)
