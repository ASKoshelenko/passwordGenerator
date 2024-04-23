import logging

def setup_logger(verbose):
    """Configure the logger's level based on the verbosity option."""
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    logger = logging.getLogger()
    logger.info('Verbose output enabled' if verbose else 'Verbose output disabled')
