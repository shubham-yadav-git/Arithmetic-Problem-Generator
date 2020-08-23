from flask import Flask, render_template, request, jsonify
import random as rn

app = Flask(__name__)

ans = 0

@app.route('/')
def home():
    return render_template("index.html")


def gen_add(no_of_add=0):
    ans_add = {}
    for i in range(int(no_of_add)):
        op1 = rn.randint(10000, 99999)
        op2 = rn.randint(10000, 99999)
        ans_add[(op1, op2)] = op1 + op2
    return ans_add


def gen_sub(num_of_sub=0):
    ans_sub = {}
    i = 0
    while i < num_of_sub:
        op1 = rn.randint(10000, 99999)
        op2 = rn.randint(10000, 99999)
        if op1 > op2:
            ans_sub[(op1, op2)] = op1 - op2
            i += 1
    return ans_sub


def gen_mul(no_of_mul=0):
    ans_mul = {}
    for i in range(int(no_of_mul)):
        op1 = rn.randint(1000, 9999)
        op2 = rn.randint(10, 99)
        ans_mul[(op1, op2)] = op1 * op2
    return ans_mul


def gen_div(no_of_div=0):
    ans_div = {}
    for i in range(int(no_of_div)):
        op1 = rn.randint(1000, 9999)
        op2 = rn.randint(4, 20)
        quo = op1 / op2
        # round(quo, 2)
        rem = op1 % op2
        ans_div[(op1, op2)] = ("Quotient="+str(round(quo, 2)
                                               ),"Remainder="+ str(rem))
    return ans_div


@app.route('/api', methods=["POST"])
def prob_gen_api():
    add = int(request.args.get("add"))
    sub = int(request.args.get("sub"))
    mul = int(request.args.get("mul"))
    div = int(request.args.get("div"))

    p_add = gen_add(int(add))
    p_sub = gen_sub(int(sub))
    p_mul = gen_mul(int(mul))
    p_div = gen_div(int(div))

    # {add: p_add, sub: p_sub, mul: p_mul, div: p_div}
    return jsonify({"add": str(p_add), "sub": str(p_sub), "mul": str(p_mul), "div": str(p_div)})


@app.route('/generator', methods=["GET", "POST"])
def generator():
    no_of_add = int(request.form["add"])
    no_of_sub = int(request.form["sub"])
    no_of_mul = int(request.form["mult"])
    no_of_div = int(request.form["div"])

    ans_add = gen_add(no_of_add)

    ans_sub = gen_sub(no_of_sub)

    ans_mul = gen_mul(no_of_mul)

    ans_div = gen_div(no_of_div)
    f = open("ans.txt", "w")
    f.write("Addition:\n" + str(ans_add) + "\n Subtraction:\n" + str(ans_sub) + "\nMultiplication:\n" + str(
        ans_mul) + "\nDivision:\n" + str(ans_div))
    f.close()
    return render_template("index.html", q_add=ans_add, q_sub=ans_sub, q_mul=ans_mul, q_div=ans_div)



if __name__ == '__main__':
    app.run(debug=True)
