from sqlalchemy import select

from workouts_backend.models import User


def test_create_user(session):
    user = User(
        username='leo',
        email='leo@mail.com',
        password='senh123@($@$(!$ ))',
    )

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'leo@mail.com'))

    assert result.username == 'leo'
