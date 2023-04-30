from pydantic.main import BaseModel


class CheckError(AssertionError):
    pass


class CheckResult(BaseModel):
    status: bool = False
    msg: str = None
    error: Exception = None

    def __str__(self):
        return "{}: test case {},error: {} " \
            .format("passed" if self.status else "failed", self.msg, self.error)

    def __repr__(self):
        return "{}: test case {},error: {} ".format("passed" if self.status else "failed",
                                                    self.msg, self.error)

    class Config:
        arbitrary_types_allowed = True


def check_result(msg, error=None, capture=True, status=False):
    if capture:
        return CheckResult(status=status, msg=msg, error=error)
    raise CheckError(msg)
