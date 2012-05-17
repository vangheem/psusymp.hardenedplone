from wildcard.lockdown import addCommitCondition

addCommitCondition("Allow logged in on host",
    logged_in=True,
    host="backend.myhost.com")
