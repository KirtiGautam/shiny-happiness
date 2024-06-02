import logging

def setup_logging():
    logger = logging.getLogger('uvicorn.error')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        "%(asctime)s [%(process)d] [%(levelname)s] %(message)s"
    ))
    logger.addHandler(handler)

    access_logger = logging.getLogger('uvicorn.access')
    access_logger.setLevel(logging.INFO)
    access_handler = logging.StreamHandler()
    access_handler.setFormatter(logging.Formatter(
        "%(asctime)s [%(process)d] [%(levelname)s] %(message)s"
    ))
    access_logger.addHandler(access_handler)


# Set up logging
setup_logging()

config = {
    "workers": 2,
    "host": "0.0.0.0",
    "port": 2121,
    "reload": True,
    "log_level": "info",
    "access_log": True
}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.main:app", **config)
