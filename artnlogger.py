"""
Structured logging configuration for ARTN
Provides consistent logging format and centralized log management
"""
import logging
import sys
from typing import Optional
from datetime import datetime
import json
from pathlib import Path

from .config import config

class JSONFormatter(logging.Formatter):
    """JSON formatter for structured logging"""
    
    def format(self, record: logging.LogRecord) -> str:
        log_data = {
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'level': record.levelname,
            'module': record.module,
            'function': record.funcName,
            'message': record.getMessage(),
            'thread': record.threadName,
        }
        
        if hasattr(record, 'extra'):
            log_data.update(record.extra)
        
        if record.exc_info:
            log_data['exception'] = self.formatException(record.exc_info)
        
        return json.dumps(log_data)

def setup_logging(
    level: Optional[str] = None,
    log_file: Optional[str] = None,
    json_format: bool = True
) -> None:
    """
    Configure logging for ARTN
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Path to log file (