# Distributed tracing systems attach trace IDs. 
# A valid trace ID: exactly 16 characters hexadecimal only lowercase letters allowed

def valid_trace_id(trace_id):

    if len(trace_id) != 16:
        return False

    for char in trace_id:

        if char not in "0123456789abcdef":
            return False

    return True


print(valid_trace_id("a3f9b12c45d678ef"))   # True
print(valid_trace_id("A3F9B12C45D678EF"))   # False
print(valid_trace_id("xyz123"))             # False
print(valid_trace_id("12345"))              # False

