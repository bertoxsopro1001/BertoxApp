from fastapi import FastAPI
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
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .calculator {
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    text-align: center;
                    color: #333;
                }
                input[type="text"] {
                    width: 80px;
                    padding: 10px;
                    margin: 5px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                select {
                    padding: 10px;
                    margin: 5px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                button {
                    width: 100%;
                    padding: 10px;
                    background-color: #28a745;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #218838;
                }
                .result {
                    margin-top: 20px;
                    text-align: center;
                    font-size: 1.2em;
                    color: #333;
                }
            </style>
        </head>
        <body>
            <div class="calculator">
                <h1>Tan simple Calculator Load Test</h1>
                <form action="/calculate" method="get">
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
                <div class="result" id="result"></div>
            </div>
        </body>
    </html>
    """

@app.get("/calculate")
async def calculate(num1: float, operation: str, num2: float):
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
