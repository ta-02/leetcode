function numberToWords(num: number): string {
  const onesMap = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
  };

  const tensMap = {
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
  };
  if (num === 0) return "Zero";

  const getString = (n: number): string => {
    const res: string[] = [];
    const hundreds = Math.floor(n / 100);
    if (hundreds) {
      res.push(onesMap[hundreds] + " Hundred");
    }
    const lastTwo = n % 100;
    if (lastTwo >= 20) {
      const tens = Math.floor(lastTwo / 10);
      const ones = lastTwo % 10;
      res.push(tensMap[tens * 10]);
      if (ones) res.push(onesMap[ones]);
    } else if (lastTwo) {
      res.push(onesMap[lastTwo]);
    }

    return res.join(" ");
  };

  const postfix = ["", " Thousand", " Million", " Billion"];
  const res: string[] = [];
  let i = 0;
  while (num) {
    const digits = num % 1000;
    const s = getString(digits);
    if (s) {
      res.push(s + postfix[i]);
    }
    num = Math.floor(num / 1000);
    i++;
  }
  return res.reverse().join(" ");
}
