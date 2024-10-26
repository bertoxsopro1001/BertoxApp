from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Simple Calculator</title>
            <style>
                input[type="text"] {
                    width: 50px;
                }
            </style>
        </head>
        <body>
            <h1>Simple Calculator</h1>
            <form action="/calculate" method="post">
                <input type="text" name="num1" placeholder="Number 1" required>
                <select name="operation" required>
                    <option value="+">+</option>
                    <option value="-">-</option>
                    <option value="*">*</option>
                    <option value="/">/</option>
                </select>
                <input type="text" name="num2" placeholder="Number 2" required>
                <button type="submit">Calculate</button>
            </form>
            <div id="result"></div>
        </body>
    </html>
    """

@app.post("/calculate")
async def calculate(num1: float = Form(...), operation: str = Form(...), num2: float = Form(...)):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            return {"error": "Division by zero is not allowed."}
        result = num1 / num2
    else:
        return {"error": "Invalid operation."}
    
    return {"result": result}
