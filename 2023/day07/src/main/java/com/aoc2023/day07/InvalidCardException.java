package com.aoc2023.day07;

public class InvalidCardException extends RuntimeException {
    InvalidCardException(String message) {
        super(message);
    }
}
