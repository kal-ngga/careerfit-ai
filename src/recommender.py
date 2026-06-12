def generate_domain_recommendation(dominant_domain):
    domain_recommendations = {
        "data science": (
            "Untuk bidang Data Science, tambahkan detail seperti data cleaning, exploratory data analysis, "
            "model machine learning, metrik evaluasi, visualisasi, dashboard, dan deployment."
        ),
        "software engineering": (
            "Untuk bidang Software Engineering, tambahkan tech stack, fitur yang dibuat, API, database, "
            "testing, deployment, link GitHub, dan link demo jika ada."
        ),
        "design": (
            "Untuk bidang Design/UI UX, tambahkan case study, problem statement, proses riset, user flow, "
            "wireframe, prototype, usability testing, dan link portfolio Figma/Behance."
        ),
        "marketing": (
            "Untuk bidang Marketing, tambahkan metrik campaign seperti reach, impressions, engagement rate, "
            "CTR, conversion rate, leads, growth followers, atau hasil campaign."
        ),
        "accounting": (
            "Untuk bidang Accounting, tambahkan pengalaman jurnal, general ledger, laporan keuangan, "
            "rekonsiliasi, pajak, audit, budgeting, dan software akuntansi."
        ),
        "finance": (
            "Untuk bidang Finance, tambahkan pengalaman financial analysis, budgeting, forecasting, "
            "financial modeling, ratio analysis, dan penggunaan Excel."
        ),
        "human resources": (
            "Untuk bidang Human Resources, tambahkan pengalaman recruitment, candidate screening, onboarding, "
            "training, payroll, dan administrasi karyawan."
        ),
        "administration": (
            "Untuk bidang Administration, tambahkan pengalaman document management, scheduling, data entry, "
            "reporting, Microsoft Office, dan koordinasi operasional."
        ),
        "sales": (
            "Untuk bidang Sales, tambahkan pencapaian seperti jumlah leads, conversion rate, revenue, "
            "target achievement, customer retention, dan penggunaan CRM."
        ),
        "customer support": (
            "Untuk bidang Customer Support, tambahkan pengalaman menangani pelanggan, complaint handling, "
            "response time, customer satisfaction, dan tools CRM/helpdesk."
        ),
        "general": (
            "Tambahkan pengalaman, skill, pencapaian, dan keyword yang paling relevan dengan job description."
        )
    }

    return domain_recommendations.get(
        dominant_domain,
        domain_recommendations["general"]
    )


def generate_score_recommendation(final_score):
    if final_score < 50:
        return (
            "CV kamu masih kurang cocok dengan job description ini. Fokuskan CV pada pengalaman, skill, "
            "tools, dan pencapaian yang paling relevan dengan posisi tersebut."
        )

    if final_score < 75:
        return (
            "CV kamu cukup relevan, tetapi masih bisa ditingkatkan. Tambahkan keyword penting dari job description "
            "dan perjelas pengalaman yang paling berhubungan dengan posisi ini."
        )

    return (
        "CV kamu sudah cukup kuat untuk lowongan ini. Tetap lengkapi requirement yang belum muncul agar peluang match semakin tinggi."
    )


def generate_missing_skill_recommendation(missing_core_skills, missing_skills):
    recommendations = []

    if missing_core_skills:
        top_core = missing_core_skills[:5]
        recommendations.append(
            "Core requirement yang belum terlihat di CV kamu: "
            + ", ".join(top_core)
            + ". Jika kamu memang memiliki kemampuan ini, tuliskan secara eksplisit."
        )

    if missing_skills:
        top_missing = missing_skills[:7]
        recommendations.append(
            "Requirement tambahan yang belum terlihat: "
            + ", ".join(top_missing)
            + "."
        )

    if not missing_core_skills and not missing_skills:
        recommendations.append(
            "Sebagian besar requirement utama dari job description sudah terdeteksi di CV kamu."
        )

    return recommendations


def generate_general_cv_recommendation():
    return (
        "Tambahkan pencapaian yang terukur, misalnya jumlah project, peningkatan performa, efisiensi waktu, "
        "jumlah pelanggan yang ditangani, revenue, engagement, akurasi model, atau output kerja yang relevan."
    )


def generate_recommendations(
    final_score,
    missing_skills,
    missing_core_skills,
    dominant_domain
):
    recommendations = []
    recommendations.append(generate_score_recommendation(final_score))
    recommendations.extend(
        generate_missing_skill_recommendation(
            missing_core_skills=missing_core_skills,
            missing_skills=missing_skills
        )
    )

    recommendations.append(generate_general_cv_recommendation())
    recommendations.append(generate_domain_recommendation(dominant_domain))

    return recommendations