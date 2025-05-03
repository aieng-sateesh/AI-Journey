# Day 4 - Python Dictionary Exercises
# Author: Sateesh Kumar
# Date: 04/05/2025

# 🧠 A dictionary of AI tools and their creators
ai_tool_name = {
    "TensorFlow": "Google",
    "PyTorch": "Meta",
    "Scikit-Learn": "Community",
    "Numpy": "Travis Oliphant"
}

# 🛠️ Updating the creator of Scikit-Learn
ai_tool_name["Scikit-Learn"] = "Google-backed"

# ❌ Deleting PyTorch entry
del ai_tool_name["PyTorch"]

# ✅ Printing updated dictionary
print("📘 Updated AI Tools Dictionary:")
print(ai_tool_name)

# 🔍 Accessing and printing individual entries
print(f"Tool: TensorFlow | Created By: {ai_tool_name['TensorFlow']}")
print(f"Tool: Scikit-Learn | Created By: {ai_tool_name['Scikit-Learn']}")
print(f"Tool: Numpy | Created By: {ai_tool_name['Numpy']}")
