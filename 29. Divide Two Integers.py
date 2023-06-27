def divide(dividend, divisor):
        # Determine the sign of the result
        sign = -1 if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0) else 1

        # Take the absolute values of dividend and divisor
        dividend = abs(dividend)
        divisor = abs(divisor)

        print([i for i in range(divisor , dividend + 1, divisor)])
        # Calculate the quotient using division and obtain the result
        result = len(range(1, dividend - divisor + 2, divisor))

        # Apply the sign to the result
        if sign == -1:
            result = -result

        # Constrain the result within the specified limits
        result = min(max(result, -(2 ** 31)), 2 ** 31 - 1)

        # Return the final result
        return result



