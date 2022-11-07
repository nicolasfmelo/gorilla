

class Gorilla:
    """
    """

    def __init__(self) -> None:
        ...
    




class Inference:
    """
    Gorilla Inference use ONNX and TFLITE Engines for Inference Models.
    """
    BACKENDS = ["tensorflow", "torch", "onnx", "tflite"]

    def __init__(self, backend: str) -> None:

        self.backend = self._check_backend(backend)

        ...
    

    def _create_backend(self):

        ...
    

    def inference(self):
        ...


    def _check_backend(self, backend: str):
        if backend.lower() in self.BACKENDS:
            return backend
        else:
            raise NameError(f"Suported Backends {' '.join(self.BACKENDS)}")


