import logging

class LogGen:

    def loggen():
        fileHandler = logging.FileHandler("C:\\Users\\vinothsc\\PycharmProjects\\orange_pro2\\Log\\filename.log")
        logger = logging.getLogger()
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s',
                                      datefmt='%d/%m/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger













