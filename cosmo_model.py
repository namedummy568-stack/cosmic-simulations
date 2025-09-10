def calculate_omega_m(omega_b, omega_c):
    """Calculates the total matter density parameter."""
    return omega_b + omega_c

def calculate_hubble_parameter(h0, z):
    """Calculates the Hubble parameter at a given redshift."""
    return h0 * (1 + z)