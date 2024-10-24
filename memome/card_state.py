from memome.utils.sgs_enum import SGSEnum


class CardState(SGSEnum):
    SLEEPING = SGSEnum("SLEEPING", 1)
    TO_REVIEW = SGSEnum("TO_REVIEW", 2)
    OUT_OF_DATE = SGSEnum("OUT_OF_DATE", 4)
