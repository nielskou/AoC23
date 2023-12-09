IDENTIFICATION DIVISION.
PROGRAM-ID. AdventOfCodeDay6.

DATA DIVISION.
WORKING-STORAGE SECTION.
    01 MilliSeconds    PIC 9(18) VALUE 59796575.
    01 MilliMeters     PIC 9(18) VALUE 597123410321328.
    01 ResultSquared   PIC 9(18).
    01 Result          PIC 9(18).
    01 Improvement     PIC 9(18).

PROCEDURE DIVISION.
    MULTIPLY MilliSeconds BY MilliSeconds.
    MULTIPLY 4 BY MilliMeters.
    SUBTRACT MilliMeters FROM MilliSeconds GIVING ResultSquared.

    MOVE ResultSquared TO Result.
    PERFORM ApproximateRoot 100 TIMES.

    DISPLAY Result.
    STOP RUN.

ApproximateRoot SECTION.
    DIVIDE ResultSquared BY Result GIVING Improvement.
    ADD Improvement TO Result.
    DIVIDE Result BY 2 GIVING Result.
    EXIT.
