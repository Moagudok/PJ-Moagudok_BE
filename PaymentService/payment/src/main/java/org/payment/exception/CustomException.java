package org.payment.exception;

public class CustomException extends RuntimeException {
    private final ErrorCode errorCode;

    public ErrorCode getErrorCode() {
        return this.errorCode;
    }

    public CustomException(final ErrorCode errorCode) {
        this.errorCode = errorCode;
    }
}
