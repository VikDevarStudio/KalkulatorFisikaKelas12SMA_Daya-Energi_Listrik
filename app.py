from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Ambil input dari form
            W = request.form.get('work')
            t = request.form.get('time')
            V = request.form.get('voltage')
            I = request.form.get('current')
            R = request.form.get('resistance')
            E = request.form.get('energy')
            P = request.form.get('power')

            # Konversi input ke tipe float jika ada
            W = float(W) if W else None
            t = float(t) if t else None
            V = float(V) if V else None
            I = float(I) if I else None
            R = float(R) if R else None
            E = float(E) if E else None
            P = float(P) if P else None

            # Hitung daya dari W / t jika W dan t tersedia
            if W is not None and t is not None:
                if t > 0:
                    P = W / t
                else:
                    P = 'Error: Waktu harus lebih dari nol'

            # Hitung energi dari P × t jika P dan t tersedia
            if P is not None and t is not None:
                E_p_t = P * t
            else:
                E_p_t = None

            # Hitung energi dari I² × R × t jika I, R, dan t tersedia
            if I is not None and R is not None and t is not None:
                E_i_r_t = I**2 * R * t
            else:
                E_i_r_t = None

            # Hitung energi dari V² / R × t jika V, R, dan t tersedia
            if V is not None and R is not None and t is not None:
                E_v2_r_t = (V**2 / R) * t
            else:
                E_v2_r_t = None

            # Hitung energi dari V × I × t jika V, I, dan t tersedia
            if V is not None and I is not None and t is not None:
                E_v_i_t = V * I * t
            else:
                E_v_i_t = None

            # Hitung daya dari V × I jika V dan I tersedia
            if V is not None and I is not None:
                P_v_i = V * I
            else:
                P_v_i = None

            # Hitung daya dari I² × R jika I dan R tersedia
            if I is not None and R is not None:
                P_i_r = I**2 * R
            else:
                P_i_r = None

            # Hitung daya dari V² / R jika V dan R tersedia
            if V is not None and R is not None:
                P_v2_r = V**2 / R
            else:
                P_v2_r = None

            # Hitung tegangan dari daya dan arus jika P dan I tersedia
            if P is not None and I is not None:
                V_from_P_I = P / I
            else:
                V_from_P_I = None

            # Hitung tegangan dari energi, arus, dan waktu jika E, I, dan t tersedia
            if E is not None and I is not None and t is not None:
                V_from_E_I_T = E / (I * t)
            else:
                V_from_E_I_T = None

            # Hitung tegangan dari daya dan resistansi (akar kuadrat) jika P dan R tersedia
            if P is not None and R is not None:
                V_sqrt_P_R = math.sqrt(P * R)
            else:
                V_sqrt_P_R = None

            # Hitung tegangan dari energi, resistansi, dan waktu (akar kuadrat) jika E, R, dan t tersedia
            if E is not None and R is not None and t is not None:
                V_sqrt_E_R_T = math.sqrt((E * R) / t)
            else:
                V_sqrt_E_R_T = None

            # Hitung waktu dari energi dan daya jika E dan P tersedia
            if E is not None and P is not None:
                T_from_E_P = E / P
            else:
                T_from_E_P = None

            # Hitung waktu dari energi, tegangan, dan arus jika E, V, dan I tersedia
            if E is not None and V is not None and I is not None:
                T_from_E_V_I = E / (V * I)
            else:
                T_from_E_V_I = None

            # Hitung waktu dari energi, arus kuadrat, dan resistansi jika E, I, dan R tersedia
            if E is not None and I is not None and R is not None:
                T_from_E_I_R = E / (I**2 * R)
            else:
                T_from_E_I_R = None

            # Hitung waktu dari energi, resistansi, dan tegangan kuadrat jika E, R, dan V tersedia
            if E is not None and R is not None and V is not None:
                T_from_E_R_V2 = (E * R) / (V**2)
            else:
                T_from_E_R_V2 = None

            # Hitung arus dari daya dan tegangan jika P dan V tersedia
            if P is not None and V is not None:
                I_from_P_V = P / V
            else:
                I_from_P_V = None

            # Hitung arus dari daya dan resistansi (akar kuadrat) jika P dan R tersedia
            if P is not None and R is not None:
                I_sqrt_P_R = math.sqrt(P / R)
            else:
                I_sqrt_P_R = None

            # Hitung arus dari energi, tegangan, dan waktu jika E, V, dan t tersedia
            if E is not None and V is not None and t is not None:
                I_from_E_V_T = E / (V * t)
            else:
                I_from_E_V_T = None

            # Hitung arus dari energi, resistansi, dan waktu (akar kuadrat) jika E, R, dan t tersedia
            if E is not None and R is not None and t is not None:
                I_sqrt_E_R_T = math.sqrt(E / (R * t))
            else:
                I_sqrt_E_R_T = None

            # Hitung resistansi dari daya dan arus kuadrat jika P dan I tersedia
            if P is not None and I is not None:
                R_from_P_I2 = P / (I**2)
            else:
                R_from_P_I2 = None

            # Hitung resistansi dari tegangan kuadrat dan daya jika V dan P tersedia
            if V is not None and P is not None:
                R_from_V2_P = V**2 / P
            else:
                R_from_V2_P = None

            # Hitung resistansi dari tegangan kuadrat, energi, dan waktu jika V, E, dan t tersedia
            if V is not None and E is not None and t is not None:
                R_from_V2_E_T = V**2 / (E * t)
            else:
                R_from_V2_E_T = None

            # Hitung resistansi dari energi dan arus kuadrat dibagi waktu jika E, I, dan t tersedia
            if E is not None and I is not None and t is not None:
                R_from_E_I2_T = E / (I**2 * t)
            else:
                R_from_E_I2_T = None

            result = {
                'P': P,
                'P_v_i': P_v_i,
                'P_i_r': P_i_r,
                'P_v2_r': P_v2_r,
                'E_v_i_t': E_v_i_t,
                'E_p_t': E_p_t,
                'E_i_r_t': E_i_r_t,
                'E_v2_r_t': E_v2_r_t,
                'V_from_P_I': V_from_P_I,
                'V_from_E_I_T': V_from_E_I_T,
                'V_sqrt_P_R': V_sqrt_P_R,
                'V_sqrt_E_R_T': V_sqrt_E_R_T,
                'T_from_E_P': T_from_E_P,
                'T_from_E_V_I': T_from_E_V_I,
                'T_from_E_I_R': T_from_E_I_R,
                'T_from_E_R_V2': T_from_E_R_V2,
                'I_from_P_V': I_from_P_V,
                'I_sqrt_P_R': I_sqrt_P_R,
                'I_from_E_V_T': I_from_E_V_T,
                'I_sqrt_E_R_T': I_sqrt_E_R_T,
                'R_from_P_I2': R_from_P_I2,
                'R_from_V2_P': R_from_V2_P,
                'R_from_V2_E_T': R_from_V2_E_T,
                'R_from_E_I2_T': R_from_E_I2_T
            }
        except ValueError:
            result = 'Error: Input tidak valid'
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
