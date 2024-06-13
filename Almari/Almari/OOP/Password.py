class Password:
    """This class is used as mixin that is inherited by user classes to provide password related functionality.:
    1.Encrypt password which then hashed by django's make_password function to increase security.
    2.Password strength indicator.
    3.Password reset functionality."""
    def encrypt_password(self):
        """Encrypts the password using random number of iterations."""
        