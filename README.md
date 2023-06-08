# Pyright bug example

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
pyright
```

```
/home/serg/src/pyright-examples/example.py
  /home/serg/src/pyright-examples/example.py:5:24 - error: Expression of type "tuple[Type[DjangoFilterBackend]]" cannot be assigned to declared type "Sequence[Type[_FilterBackendProtocol]]"
    "DjangoFilterBackend" is incompatible with protocol "_FilterBackendProtocol"
    Type "Type[DjangoFilterBackend]" cannot be assigned to type "Type[_FilterBackendProtocol]"
      "filter_queryset" is an incompatible type
        Type "(request: Unknown, queryset: Unknown, view: Unknown) -> (Unknown | Any | QuerySet[Unknown])" cannot be assigned to type "(request: Any, queryset: _Q@filter_queryset, view: APIView) -> _Q@filter_queryset"
          Function return type "Unknown | Any | QuerySet[Unknown]" is incompatible with type "_Q@filter_queryset"
            Type "Unknown | Any | QuerySet[Unknown]" cannot be assigned to type "_Q@filter_queryset" (reportGeneralTypeIssues)
1 error, 0 warnings, 0 informations
```
