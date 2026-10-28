import logging

logger = logging.getLogger('ConverterLogger')
logger.setLevel(logging.DEBUG)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


class Converter:
    @staticmethod
    def do(x: float) -> int:
        logger.debug(f"Входной параметр: x = {x}")

        if x >= 100.7:
            logger.info(f"x >= 100.7 -> возврат 1000")
            return 1000

        if 0 < x < 100.7:
            result = int(x)
            logger.info(f"0 < x < 100.7 -> возврат {result}")
            return result

        if x == 0.0:
            logger.error("x == 0.0 -> ValueError")
            raise ValueError("x не может быть равен 0.0")

        if -30.4 <= x < 0:
            result = int(x) - 5
            logger.info(f"-30.4 <= x < 0 -> возврат {result}")
            return result

        # x <= -30.5
        logger.info(f"x <= -30.5 -> возврат -2000")
        return -2000