package com.aoc2023.day07;

import java.util.Comparator;

public enum Card  {
    CARD_2,
    CARD_3,
    CARD_4,
    CARD_5,
    CARD_6,
    CARD_7,
    CARD_8,
    CARD_9,
    CARD_T,
    CARD_J,
    CARD_Q,
    CARD_K,
    CARD_A;

    public static Card fromChar(Character c) {
        if (c == 'A') {
            return CARD_A;
        } else if (c == 'K') {
            return CARD_K;
        } else if (c == 'Q') {
            return CARD_Q;
        } else if (c == 'J') {
            return CARD_J;
        } else if (c == 'T') {
            return CARD_T;
        } else if (c == '9') {
            return CARD_9;
        } else if (c == '8') {
            return CARD_8;
        } else if (c == '7') {
            return CARD_7;
        } else if (c == '6') {
            return CARD_6;
        } else if (c == '5') {
            return CARD_5;
        } else if (c == '4') {
            return CARD_4;
        } else if (c == '3') {
            return CARD_3;
        } else if (c == '2') {
            return CARD_2;
        } else {
            throw new InvalidCardException("no such card " + c);
        }
    }

}

class CardComparator implements Comparator<Card> {
    @Override
    public int compare(Card card1, Card card2) {
        return card1.ordinal() - card2.ordinal();
    }
}
