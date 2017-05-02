function SeriesSum(n) {
  for (var s=0, i=0; i<n; i++){
  s += 1/(3*i+1);
  }
  return (s.toFixed(2));

}


// SeriesSum(1) => 1 = "1"
// SeriesSum(2) => 1 + 1/4 = "1.25"
// SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"
