import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import 'template_bloc.dart';
import 'template_view.dart';

class TemplateProvider extends BlocProvider<TemplateBloc> {
  TemplateProvider({
    Key key,
  }) : super(
          key: key,
          create: (context) => TemplateBloc(context),
          child: TemplateView(),
        );
}
