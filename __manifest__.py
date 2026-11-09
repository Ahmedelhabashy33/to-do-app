{
    'name': "to_do_app",
    'author': "Ahmed Elhabashy",
    'category': "Custom",
    'version': "17.0.1.0.0",
    'depends': ['base' , 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_task_view.xml',
        'views/base_menu.xml',
        ],
    'license': 'LGPL-3',
    'application': True,
    'installable': True,

}
