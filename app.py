from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>DevOps Dashboard</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gradient-to-br from-gray-900 via-blue-900 to-indigo-900 min-h-screen text-white">

    <div class="max-w-5xl mx-auto p-8">

        <!-- Header -->
        <div class="text-center mb-10">
            <h1 class="text-4xl font-bold">🚀 DevOps Dashboard</h1>
            <p class="text-gray-300 mt-2">Application Flask + Docker + Jenkins</p>
        </div>

        <!-- Cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">

            <div class="bg-white/10 p-6 rounded-2xl shadow-lg backdrop-blur">
                <h2 class="text-xl font-bold">🐳 Docker</h2>
                <p class="text-gray-300 mt-2">Containerisation de l'application</p>
            </div>

            <div class="bg-white/10 p-6 rounded-2xl shadow-lg backdrop-blur">
                <h2 class="text-xl font-bold">⚙️ Jenkins</h2>
                <p class="text-gray-300 mt-2">CI/CD Pipeline automatisé</p>
            </div>

            <div class="bg-white/10 p-6 rounded-2xl shadow-lg backdrop-blur">
                <h2 class="text-xl font-bold">☸️ Kubernetes</h2>
                <p class="text-gray-300 mt-2">Déploiement scalable</p>
            </div>

        </div>

        <!-- Section tableau -->
        <div class="mt-10 bg-white/10 p-6 rounded-2xl backdrop-blur">

            <h2 class="text-2xl font-bold mb-4">📚 Liste des étudiants</h2>

            <table class="w-full text-left">
                <thead>
                    <tr class="border-b border-gray-500">
                        <th class="py-2">Nom</th>
                        <th>Prénom</th>
                        <th>Note</th>
                        <th>Mention</th>
                    </tr>
                </thead>

                <tbody class="text-gray-200">
                    <tr class="border-b border-gray-700">
                        <td class="py-2">Dione</td>
                        <td>Aminata</td>
                        <td>16</td>
                        <td>Très bien</td>
                    </tr>

                    <tr class="border-b border-gray-700">
                        <td class="py-2">Sow</td>
                        <td>Moussa</td>
                        <td>14</td>
                        <td>Bien</td>
                    </tr>

                    <tr class="border-b border-gray-700">
                        <td class="py-2">Ba</td>
                        <td>Fatou</td>
                        <td>12</td>
                        <td>Assez bien</td>
                    </tr>

                    <tr>
                        <td class="py-2">Diallo</td>
                        <td>Ibrahima</td>
                        <td>9</td>
                        <td>Insuffisant</td>
                    </tr>
                </tbody>
            </table>

        </div>

        <div class="text-center mt-10 text-gray-400">
            Projet DevOps - Flask + Docker + Jenkins 🚀
        </div>

    </div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)