import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cvxpy as cp

# 시스템 파라미터 정의
N = 10  # 예측 시간 길이
dt = 1  # 시간 간격
initial_position = 5.0  # 초기 위치
velocity = 0.0  # 초기 속도
target = 0  # 목표 위치
max_force = 1.0  # 최대 제어 입력

# 초기 상태 정의
state = np.array([initial_position, velocity])

# MPC 제어 함수
def mpc_control(state, target):
    x = cp.Variable((2, N+1))
    u = cp.Variable((1, N))
    cost = 0
    constraints = []

    A = np.array([[1, dt], [0, 1]])
    B = np.array([[0], [dt]])

    for t in range(N):
        cost += cp.quad_form(x[:, t] - np.array([target, 0]), np.eye(2))  # 상태 오차에 대한 비용
        cost += cp.quad_form(u[:, t], np.eye(1))  # 입력에 대한 비용
        constraints += [x[:, t+1] == A @ x[:, t] + B @ u[:, t]]  # 시스템 동역학
        constraints += [cp.abs(u[:, t]) <= max_force]  # 제어 입력의 제한

    constraints += [x[:, 0] == state]  # 초기 상태

    prob = cp.Problem(cp.Minimize(cost), constraints)
    prob.solve()

    return u.value[0, 0]  # 첫 번째 제어 입력 반환

# 키보드 입력 처리 함수
def on_key_press(event):
    global state
    if event.key == 'left':
        state[0] -= 1.0
    elif event.key == 'right':
        state[0] += 1.0

# 시뮬레이션 설정
t_final = 10
num_steps = int(t_final / dt)
positions = np.zeros(num_steps)
times = np.linspace(0, t_final, num_steps)

# 초기 조건
positions[0] = initial_position

# 애니메이션 설정
fig, ax = plt.subplots()
ax.set_xlim(-6, 6)
ax.set_ylim(-1, 1)
line, = ax.plot([], [], 'o-', lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    global state
    control_input = mpc_control(state, target)
    state = np.array([state[0] + state[1] * dt, state[1] + control_input * dt])
    positions[i] = state[0]
    line.set_data([state[0]], [0])
    return line,

fig.canvas.mpl_connect('key_press_event', on_key_press)
ani = animation.FuncAnimation(fig, animate, frames=num_steps, init_func=init, blit=True)

plt.show()
