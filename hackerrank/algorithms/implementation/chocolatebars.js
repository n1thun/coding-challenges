function getWays(squares, d, m) {
  count = 0;

  for (i = 0; i < squares.length-(m-1); i++) {
    stepper = 0;
    sum = 0;
    do {
        sum += squares[i+stepper];
        stepper++;
        //console.log(sum);
      }
      while (stepper < m);
      if (sum === d) {
      count++;
    }
    }
      return count;
  }
