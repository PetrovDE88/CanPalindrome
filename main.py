def can_palindrome(s: str) -> bool:
    symbols={}
    for symbol in s:
        symbols[symbol] = symbols.get(symbol, 0) + 1
    number_symbols=len(symbols)
    count=0
    for numbers in symbols.values():
        if numbers%2==0:
            count+=1
    return count==number_symbols or count==number_symbols-1


if __name__ == '__main__':
    input_s = input('Введите строку: ')
    if can_palindrome(input_s):
        print('Можно сделать палиндромом')
    else:
        print('Нельзя сделать палиндромом')