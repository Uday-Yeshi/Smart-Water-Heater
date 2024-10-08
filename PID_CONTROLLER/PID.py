class PIDController:
    def __init__(self, Kp, Ki, Kd, set_point):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.set_point = set_point
        self.previous_error = 0
        self.integral = 0

    def compute(self, current_value, dt):
        # Calculate error
        error = self.set_point - current_value
        
        # Proportional term
        P = self.Kp * error
        
        # Integral term
        self.integral += error * dt
        I = self.Ki * self.integral
        
        # Derivative term
        derivative = (error - self.previous_error) / dt
        D = self.Kd * derivative
        
        # Update previous error
        self.previous_error = error
        
        # Calculate output
        output = P + I + D
        
        return output

# Example usage
if __name__ == "__main__":
    import time
    import random
    
    # PID controller parameters
    Kp = 1.0
    Ki = 0.1
    Kd = 0.01
    set_point = 100  # Desired set point
    
    # Initialize PID controller
    pid = PIDController(Kp, Ki, Kd, set_point)
    
    # Simulate a system
    current_value = 0
    dt = 0.1  # Time step
    for _ in range(100):
        # Simulate some process
        current_value += random.uniform(-0.5, 0.5)  # Random noise
        
        # Compute PID output
        control_signal = pid.compute(current_value, dt)
        
        # Apply control signal to the system (for simulation purposes, we simply add it to the current value)
        current_value += control_signal
        
        # Print current state
        print(f"Current Value: {current_value}, Control Signal: {control_signal}")
        
        # Wait for next time step
        time.sleep(dt)
