import sys


def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()    # returns in exc_tb: information of file name, line no., etc where exception occured

    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name: [{0}], line number: [{1}], error message: [{2}]".format(
        filename, exc_tb.tb_lineno, str(error)
    )   # custom error message with line number

    return error_message


class CustomException(Exception):                               # inherited 'Exception' class
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)                           # initialized the 'Exception' class
        self.error_message = error_message_detail(error_message, error_detail=error_detail)


    def __str__(self):              # Prints the error message when the class called
        return self.error_message




# import logging
# if __name__=="__main__":
#     try: a=1/0
#     except Exception as e:
#         logging.info("Divide by zero")
#         raise CustomException(e, sys)
        
