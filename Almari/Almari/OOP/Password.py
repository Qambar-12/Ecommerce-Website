class Password:
    """This class is used as mixin that is inherited by user classes to provide password related functionality.:
    1.Encrypt password which then hashed by django's make_password function to increase security.
    2.Password strength indicator.
    3.Password reset functionality."""
    @staticmethod
    def encrypt_password_signup(plain_password,username,role):
        """Encrypts the password using random number of iterations."""
        import random
        # Used to store the random number used to encrypt the password in a 2D list
        increment_val = []
        encrypted = plain_password
        
        # Random number of iterations between 1 and 5
        iterations = random.randint(1, 5)
        
        for _ in range(iterations):
            new_encrypted = ''
            iteration_increments = []
            for ch in encrypted:
                increment = random.randint(0, 50)
                # The ASCII value of each character in the password is incremented by a random number
                new_encrypted += chr(ord(ch) + increment)
                iteration_increments.append(increment)
            encrypted = new_encrypted
            increment_val.append(iteration_increments)
        
        # Save the 2D list in a file named after the username in appropriate directory
        with open(f"encryption_keys/{role}/{username}.txt", "w") as key_file:
            key_file.write(str(increment_val))
        
        return encrypted
    @staticmethod
    def encrypt_password_login(plain_password,username,role):
        """Encrypts the password using the key read from the file."""
        key = Password.read_encryption_key(username,role)
        encrypted = plain_password
        
        for iteration_increments in key:
            new_encrypted = ''
            for i, ch in enumerate(encrypted):
                # The ASCII value of each character in the password is decremented by the corresponding number in the key
                new_encrypted += chr(ord(ch) - iteration_increments[i])
            encrypted = new_encrypted
        return encrypted
    @staticmethod
    def read_encryption_key(username,role):
        """Reads the encryption key from the file."""
        with open(f"encryption_keys/{role}/{username}.txt", "r") as key_file:
            return eval(key_file.read())
        