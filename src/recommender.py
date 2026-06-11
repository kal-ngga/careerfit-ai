def generate_recommendations(final_score, missing_skills):
    recommendations = []

    if final_score < 50:
        recommendations.append(
            "CV kamu masih kurang cocok dengan job description ini. "
            "Coba sesuaikan pengalaman, skill, dan project yang paling relevan."
        )

    elif final_score < 75:
        recommendations.append(
            "CV kamu cukup relevan, tetapi masih bisa ditingkatkan dengan "
            "menambahkan keyword dan pengalaman yang lebih sesuai."
        )

    else:
        recommendations.append(
            "CV kamu sudah cukup kuat untuk lowongan ini. "
            "Tetap perbaiki bagian skill yang belum muncul agar lebih maksimal."
        )

    if len(missing_skills) > 0:
        top_missing_skills = missing_skills[:5]

        recommendations.append(
            "Beberapa skill yang belum terlihat di CV kamu: " + ", ".join(top_missing_skills) + "."
        )

        recommendations.append(
            "Jika kamu memang memiliki skill tersebut, "
            "tambahkan secara eksplisit di bagian Skills atau Project Experience."
        )

    else:
        recommendations.append(
            "Semua skill utama dari job description sudah terdeteksi di CV kamu."
        )

    recommendations.append(
        "Tambahkan impact yang terukur pada project, misalnya akurasi model, "
        "jumlah data, tools yang digunakan, atau hasil deployment."
    )

    return recommendations